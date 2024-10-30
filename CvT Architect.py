CvT(
  (stage1_conv_embed): Sequential(
    (0): Conv2d(3, 64, kernel_size=(7, 7), stride=(4, 4), padding=(2, 2))
    (1): Rearrange('b c h w -> b (h w) c', h=56, w=56)
    (2): LayerNorm((64,), eps=1e-05, elementwise_affine=True)
  )
  (stage1_transformer): Sequential(
    (0): Transformer(
      (layers): ModuleList(
        (0): ModuleList(
          (0): PreNorm(
            (norm): LayerNorm((64,), eps=1e-05, elementwise_affine=True)
            (fn): ConvAttention(
              (to_q): SepConv2d(
                (depthwise): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_k): SepConv2d(
                (depthwise): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_v): SepConv2d(
                (depthwise): Conv2d(64, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=64)
                (bn): BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(64, 64, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_out): Identity()
            )
          )
          (1): PreNorm(
            (norm): LayerNorm((64,), eps=1e-05, elementwise_affine=True)
            (fn): FeedForward(
              (net): Sequential(
                (0): Linear(in_features=64, out_features=256, bias=True)
                (1): GELU(approximate='none')
                (2): Dropout(p=0.0, inplace=False)
                (3): Linear(in_features=256, out_features=64, bias=True)
                (4): Dropout(p=0.0, inplace=False)
              )
            )
          )
        )
      )
    )
    (1): Rearrange('b (h w) c -> b c h w', h=56, w=56)
  )
  (stage2_conv_embed): Sequential(
    (0): Conv2d(64, 192, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
    (1): Rearrange('b c h w -> b (h w) c', h=28, w=28)
    (2): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
  )
  (stage2_transformer): Sequential(
    (0): Transformer(
      (layers): ModuleList(
        (0-1): 2 x ModuleList(
          (0): PreNorm(
            (norm): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
            (fn): ConvAttention(
              (to_q): SepConv2d(
                (depthwise): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(192, 192, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_k): SepConv2d(
                (depthwise): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(192, 192, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_v): SepConv2d(
                (depthwise): Conv2d(192, 192, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=192)
                (bn): BatchNorm2d(192, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(192, 192, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_out): Sequential(
                (0): Linear(in_features=192, out_features=192, bias=True)
                (1): Dropout(p=0.0, inplace=False)
              )
            )
          )
          (1): PreNorm(
            (norm): LayerNorm((192,), eps=1e-05, elementwise_affine=True)
            (fn): FeedForward(
              (net): Sequential(
                (0): Linear(in_features=192, out_features=768, bias=True)
                (1): GELU(approximate='none')
                (2): Dropout(p=0.0, inplace=False)
                (3): Linear(in_features=768, out_features=192, bias=True)
                (4): Dropout(p=0.0, inplace=False)
              )
            )
          )
        )
      )
    )
    (1): Rearrange('b (h w) c -> b c h w', h=28, w=28)
  )
  (stage3_conv_embed): Sequential(
    (0): Conv2d(192, 384, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
    (1): Rearrange('b c h w -> b (h w) c', h=14, w=14)
    (2): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
  )
  (stage3_transformer): Sequential(
    (0): Transformer(
      (layers): ModuleList(
        (0-9): 10 x ModuleList(
          (0): PreNorm(
            (norm): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
            (fn): ConvAttention(
              (to_q): SepConv2d(
                (depthwise): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(384, 384, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_k): SepConv2d(
                (depthwise): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(384, 384, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_v): SepConv2d(
                (depthwise): Conv2d(384, 384, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), groups=384)
                (bn): BatchNorm2d(384, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
                (pointwise): Conv2d(384, 384, kernel_size=(1, 1), stride=(1, 1))
              )
              (to_out): Sequential(
                (0): Linear(in_features=384, out_features=384, bias=True)
                (1): Dropout(p=0.0, inplace=False)
              )
            )
          )
          (1): PreNorm(
            (norm): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
            (fn): FeedForward(
              (net): Sequential(
                (0): Linear(in_features=384, out_features=1536, bias=True)
                (1): GELU(approximate='none')
                (2): Dropout(p=0.0, inplace=False)
                (3): Linear(in_features=1536, out_features=384, bias=True)
                (4): Dropout(p=0.0, inplace=False)
              )
            )
          )
        )
      )
    )
  )
  (dropout_large): Dropout(p=0.0, inplace=False)
  (mlp_head): Sequential(
    (0): LayerNorm((384,), eps=1e-05, elementwise_affine=True)
    (1): Linear(in_features=384, out_features=4, bias=True)
  )
)