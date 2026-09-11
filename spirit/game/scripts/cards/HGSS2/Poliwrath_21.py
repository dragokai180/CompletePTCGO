from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8a62a1c2-2bde-5c18-9b45-8d037b7fa4ae',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name',
    display_name='Poliwrath',
    searchable_by=['Poliwrath', 'Stage 2', 'Poliwrath'],
    subtypes=['Stage 2'],
    collector_number=21,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Steamroll',
            game_text="Does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Dynamic Punch',
            game_text='Flip a coin. If heads, this attack does 60 damage plus 40 more damage and the Defending Pokémon is now Confused.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
