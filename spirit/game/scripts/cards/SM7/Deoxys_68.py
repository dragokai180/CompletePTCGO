from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f1c5c31-05de-52be-8ae6-2ce447489ff0',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name',
    display_name='Deoxys',
    searchable_by=['Deoxys', 'Basic', 'Deoxys'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=386,
    abilities=[
        Attack(
            title='Reflect',
            game_text="During your opponent's next turn, this Pokémon takes 40 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic Corkscrew',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
