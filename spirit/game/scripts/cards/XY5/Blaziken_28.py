from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e6f876b7-7964-5511-80c9-1c99a4d44b3e',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name',
    display_name='Blaziken',
    searchable_by=['Blaziken', 'Stage 2', 'Blaziken'],
    subtypes=['Stage 2'],
    collector_number=28,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name',
    family_id=255,
    abilities=[
        Attack(
            title='Spreading Flames',
            game_text='Attach 3 Fire Energy cards from your discard pile to your Pokémon in any way you like.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Heat Blow',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
