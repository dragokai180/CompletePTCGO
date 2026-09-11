from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e07d3a7b-fdd9-5cac-9f30-8b749486398c',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name',
    display_name='Spiritomb',
    searchable_by=['Spiritomb', 'Basic', 'Spiritomb'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=442,
    abilities=[
        Ability(
            title='Cursed Whirlpool',
            game_text="As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon can't retreat.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, your opponent's Active Pokémon can't retreat."),
        ),
        Attack(
            title='Cursed Drop',
            game_text="Put 3 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
