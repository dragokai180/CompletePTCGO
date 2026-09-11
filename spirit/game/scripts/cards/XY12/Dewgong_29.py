from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aaee9ebc-9d4b-5382-bcd5-83bd23122430',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name',
    display_name='Dewgong',
    searchable_by=['Dewgong', 'Stage 1', 'Dewgong'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name',
    family_id=86,
    abilities=[
        Attack(
            title='Super Deep Dive',
            game_text='Heal 40 damage from this Pokémon. Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Take Down',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
