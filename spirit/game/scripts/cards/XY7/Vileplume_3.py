from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='799bb55d-d79b-5cd6-91d1-f25af840b56b',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name',
    display_name='Vileplume',
    searchable_by=['Vileplume', 'Stage 2', 'Vileplume'],
    subtypes=['Stage 2'],
    collector_number=3,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Ability(
            title='Irritating Pollen',
            game_text="Each player can't play any Item cards from his or her hand.",
            passive=standard_passive("Each player can't play any Item cards from his or her hand."),
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
