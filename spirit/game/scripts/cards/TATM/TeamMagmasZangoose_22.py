from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='832fc007-ff56-594b-9af7-f7b47447eabd',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasZangoose.Name',
    display_name="Team Magma's Zangoose",
    searchable_by=["Team Magma's Zangoose", 'Basic', 'TeamMagmasZangoose'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=335,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for up to 2 Basic Team Magma Pokémon and put them onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Team Play',
            game_text='This attack does 20 damage times the number of Team Magma Pokémon on your Bench.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
