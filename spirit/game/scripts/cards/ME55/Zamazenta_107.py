from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3e101136-351b-5983-810d-ed934d293aa0',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name',
    display_name='Zamazenta',
    searchable_by=['Zamazenta', 'Basic', 'Zamazenta'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=889,
    abilities=[
        Attack(
            title='Fend Off',
            game_text="Before doing damage, discard all Pokémon Tools from your opponent's Active Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Shield Press',
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
