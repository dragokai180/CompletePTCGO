from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='33130514-8892-5139-806d-730e17cd7bf1',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name',
    display_name='Regice',
    searchable_by=['Regice', 'Basic', 'Regice'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=378,
    abilities=[
        Ability(
            title='Icy Barrier',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent can't play any Stadium cards from their hand.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent can't play any Stadium cards from their hand."),
        ),
        Attack(
            title='Icy Wind',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
