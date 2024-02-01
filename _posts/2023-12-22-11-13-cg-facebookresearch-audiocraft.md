---
layout: post
title: Meta 开源工具可以快速进行音乐创作
tags: Python
---

大家好，又见面了，我是 GitHub 精选君！

###### 背景介绍

我们生活在一个充满音乐和声音的世界，每一首歌曲、每一个音效都在传递着一种情感或信息。然而，音频的处理和生成却是一件相对复杂的事情。为了生成高质量的音频，我们不仅需要懂得音乐的规则，还需要掌握专业的音频编码技术。现有音频处理工具通常不够灵活，不能根据用户的具体需求进行定制，这就给音频创作带来了很大的限制。

今天要给大家推荐一个 GitHub 开源项目 facebookresearch/audiocraft，该项目在 GitHub 有超过 17.8k Star，用一句话介绍该项目就是：“Audiocraft is a library for audio processing and generation with deep learning. It features the state-of-the-art EnCodec audio compressor / tokenizer, along with MusicGen, a simple and controllable music generation LM with textual and melodic conditioning.”。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240127214629243.png)

###### 项目介绍

Audiocraft 是 Meta 旗下一款专门用于音频处理和生成的深度学习库。通过工具库中的 EnCodec 音频压缩器/分词器，你可以获得最前沿的音频处理技术。除此之外，Audiocraft 还设计了一个名为 MusicGen 的音乐生成模型，该模型可以通过文本和旋律条件控制，使用非常简单，同时可以生成高音质的音乐。在 PyTorch 环境下，Audiocraft 提供了详细的训练和推理代码，以供研究者和开发者使用。

![](https://raw.githubusercontent.com/ZhuPeng/pic/master/images/compress_image-20240127214742903.png)

###### 如何使用

Audiocraft 的安装需要 Python 3.9 和 PyTorch 2.0.0 的环境。你可以通过 pip 安装，或者直接从 GitHub 获取最新版本的代码。这是一个安装示例：

```shell
python -m pip install 'torch==2.1.0'
python -m pip install setuptools wheel
# 然后选择以下几种安装方式之一
python -m pip install -U audiocraft  # stable release
python -m pip install -U git+https://git@github.com/facebookresearch/audiocraft#egg=audiocraft  # bleeding edge
python -m pip install -e .  # or if you cloned the repo locally (mandatory if you want to train).
```
安装完成后，可以直接通过 Python 代码实现对音频的处理和生成。以下是一个 MusicGen 的代码示例：

```python
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

model = MusicGen.get_pretrained('facebook/musicgen-melody')
model.set_generation_params(duration=8)  # generate 8 seconds.
wav = model.generate_unconditional(4)    # generates 4 unconditional audio samples
descriptions = ['happy rock', 'energetic EDM', 'sad jazz']
wav = model.generate(descriptions)  # generates 3 samples.

melody, sr = torchaudio.load('./assets/bach.mp3')
# generates using the melody from the given audio and the provided descriptions.
wav = model.generate_with_chroma(descriptions, melody[None].expand(3, -1, -1), sr)

for idx, one_wav in enumerate(wav):
    # Will save under {idx}.wav, with loudness normalization at -14 db LUFS.
    audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)
```

###### 项目推介

Audiocraft 来自 Meta 的研究团队，项目提供了丰富的 API 文档和 FAQ，方便开发者对项目的理解和使用。


以下是该项目 Star 趋势图（代表项目的活跃程度）：

![](https://api.star-history.com/svg?repos=facebookresearch/audiocraft&type=Timeline)

更多项目详情请查看如下链接。

开源项目地址：https://github.com/facebookresearch/audiocraft 

开源项目作者：facebookresearch

以下是参与项目建设的所有成员：

![](https://contrib.rocks/image?repo=facebookresearch/audiocraft)

关注我们，一起探索有意思的开源项目。

