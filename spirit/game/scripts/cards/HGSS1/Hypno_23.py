from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='abafb459-d872-508b-98ac-d9a13cea4369',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name',
    display_name='Hypno',
    searchable_by=['Hypno', 'Stage 1', 'Hypno'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name',
    family_id=96,
    abilities=[
        Ability(
            title='Sleep Pendulum',
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, the Defending Pokémon is now Asleep. This power can't be used if Hypno is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Psychic Shot',
            game_text="Does 10 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
