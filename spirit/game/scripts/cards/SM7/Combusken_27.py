from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='00112863-ea1c-587c-85b8-a0b6a7e70242',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name',
    display_name='Combusken',
    searchable_by=['Combusken', 'Stage 1', 'Combusken'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name',
    family_id=255,
    abilities=[
        Attack(
            title='Double Kick',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
