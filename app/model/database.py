from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 定义 PostgreSQL 数据库 URL，使用 asyncpg 驱动
DATABASE_URL = "postgresql+asyncpg://postgres:123456@localhost/test"

# 创建异步引擎
engine = create_async_engine(DATABASE_URL, echo=True)

# 创建异步 session 工厂
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 基础类，用于定义模型
Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
