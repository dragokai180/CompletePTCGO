from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='313c2ffd-ca6d-518e-bc02-7677d749e7d8',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SuicuneEnteiLEGEND.Name',
    display_name='Suicune & Entei LEGEND',
    searchable_by=['Suicune & Entei LEGEND', 'LEGEND', 'SuicuneEnteiLEGEND'],
    subtypes=['LEGEND'],
    collector_number=94,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=160,
    elements=[PokemonTypes.WATER, PokemonTypes.FIRE],
    stage=PokemonStage.LEGEND,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=244,
    abilities=[
        Attack(
            title='Torrent Blade',
            game_text="Return 2 Water Energy attached to Suicune & Entei LEGEND to your hand. Choose 1 of your opponent's Benched Pokémon. This attack does 100 damage to that Pokémon. (Don't apply Weakness or Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bursting Inferno',
            game_text='The Defending Pokémon is now Burned.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
