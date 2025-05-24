# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with
code in this repository.

## Project Overview

This is a Korean personal blog powered by Pelican (static site generator) with a
custom CLI tool for content management. The blog uses a custom "clean" theme and
supports both Markdown and reStructuredText content.

## Common Commands

### Blog Management

- `uv run cli post <TITLE>` - Create a new blog post with proper metadata
  template
- `uv run cli preview` - Start development server with auto-reload (
  `pelican --autoreload --listen`)
- `uv run cli build` - Build site for production using publishconf.py
- `uv run cli clean` - Clean output directory and cache files

### Package Management

- `uv sync` - Install dependencies from uv.lock
- `uv add <package>` - Add new dependency

## Architecture

### Content Structure

- Blog posts are stored in `content/blog/YYYY/` directories
- Posts use Pelican metadata format with Title, Date, Category, Tags, Slug,
  Summary
- Images are organized in `content/img/YYYY/` matching post dates
- Content supports both Markdown (.md) and reStructuredText (.rst)

### CLI Tool (`cli/main.py`)

- Built with Cleo framework for command-line interface
- PostCmd: Generates post templates with Korean slug support
- PreviewCmd: Wrapper for Pelican development server
- BuildCmd: Production build using publishconf.py settings
- CleanCmd: Cleanup utility for output and cache directories

### Configuration

- `pelicanconf.py`: Development configuration with relative URLs
- `publishconf.py`: Production configuration with absolute URLs, analytics, and
  feeds
- Uses custom "clean" theme located in `clean/` directory
- Markdown extensions include mermaidjs, toc, codehilite, and more

### Key Features

- Korean language support with proper timezone (Asia/Seoul)
- Mermaid.js integration for diagrams
- Multiple comment systems (Utterances, Giscus)
- Google Analytics and AdSense integration in production
- Buy Me a Coffee integration
