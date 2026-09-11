from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9a2fe570-6e11-58ef-b037-ebc2b0e7d053',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name',
    display_name='Shiftry',
    searchable_by=['Shiftry', 'Stage 2', 'Shiftry'],
    subtypes=['Stage 2'],
    collector_number=7,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name',
    family_id=273,
    abilities=[
        Ability(
            title='Leaf Draw',
            game_text='Once during your turn (before your attack), you may discard a Grass Energy card from your hand. If you do, draw 3 cards.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Deranged Dance',
            game_text="This attack does 20 damage times the number of Benched Pokémon (both yours and your opponent's).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
