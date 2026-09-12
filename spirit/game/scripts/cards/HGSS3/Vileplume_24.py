from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6da164b3-22ad-5437-85c8-63a7e1606548',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name',
    display_name='Vileplume',
    searchable_by=['Vileplume', 'Stage 2', 'Vileplume'],
    subtypes=['Stage 2'],
    collector_number=24,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Ability(
            title='Allergy Flower',
            game_text="Each player can't play any Item cards from his or her hand.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Each player can't play any Item cards from his or her hand."),
        ),
        Attack(
            title='Dazzling Pollen',
            game_text='Flip a coin. If heads, this attack does 50 damage plus 20 more damage. If tails, the Defending Pokémon is now Confused.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
