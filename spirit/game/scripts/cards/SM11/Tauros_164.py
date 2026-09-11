from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3e16547-40ce-54d3-b117-8f9b81cfad92',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name',
    display_name='Tauros',
    searchable_by=['Tauros', 'Basic', 'Tauros'],
    subtypes=['Basic'],
    collector_number=164,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=128,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Berserker Tackle',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
