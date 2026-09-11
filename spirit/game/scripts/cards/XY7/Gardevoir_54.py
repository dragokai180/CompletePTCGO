from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='af29d6f6-194b-5c5b-93d3-a69530aab29c',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name',
    display_name='Gardevoir',
    searchable_by=['Gardevoir', 'Stage 2', 'Gardevoir'],
    subtypes=['Stage 2'],
    collector_number=54,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name',
    family_id=280,
    abilities=[
        Ability(
            title='Bright Heal',
            game_text='Once during your turn (before your attack), you may heal 20 damage from each of your Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Telekinesis',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
