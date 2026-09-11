from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d09f31d-0f9a-5144-874a-da8f24b55ef3',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name',
    display_name='Sceptile',
    searchable_by=['Sceptile', 'Stage 2', 'Sceptile'],
    subtypes=['Stage 2'],
    collector_number=8,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name',
    family_id=252,
    abilities=[
        Ability(
            title='Nurture and Heal',
            game_text='Once during your turn (before your attack), you may attach a Grass Energy card from your hand to 1 of your Pokémon. If you do, heal 30 damage from that Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Jungle Edge',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
