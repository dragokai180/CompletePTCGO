from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
    energy_color, energy_color_condition,
)


card = PokemonCardDef(
    guid='af80e064-f379-5ef7-99ef-3ed4383dd858',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name',
    display_name='Vivillon',
    searchable_by=['Vivillon', 'Stage 2', 'Vivillon'],
    subtypes=['Stage 2'],
    collector_number=15,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name',
    family_id=664,
    abilities=[
        Ability(
            title='Energy Color',
            game_text='Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a basic Energy card and attach it to 1 of your Pokémon. Shuffle your deck afterward.',
            effect=energy_color,
            condition=energy_color_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Sleep Powder',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
