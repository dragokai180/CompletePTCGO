from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bbfbda70-3391-599b-b509-a7b2376aa4a9',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name',
    display_name='Manaphy',
    searchable_by=['Manaphy', 'Basic', 'Manaphy'],
    subtypes=['Basic'],
    collector_number=42,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=490,
    abilities=[
        Attack(
            title='Deep Currents',
            game_text='Shuffle 5 Water Energy cards from your discard pile into your deck.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Water Pulse',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
