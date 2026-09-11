from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e6e024e-967e-5df4-a4c6-69337b6ef1d5',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name',
    display_name='Steelix',
    searchable_by=['Steelix', 'Stage 1', 'Steelix'],
    subtypes=['Stage 1'],
    collector_number=89,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name',
    family_id=95,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Tail Crush',
            game_text='Flip a coin. If heads, this attack does 40 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
