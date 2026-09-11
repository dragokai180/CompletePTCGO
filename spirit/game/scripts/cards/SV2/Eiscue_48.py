from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='88a68e3c-ed0f-5071-9934-8ede055f20bd',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name',
    display_name='Eiscue',
    searchable_by=['Eiscue', 'Basic', 'Eiscue'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=875,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Frigid Block',
            game_text="Discard all Energy from this Pokémon. During your opponent's next turn, this Pokémon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
