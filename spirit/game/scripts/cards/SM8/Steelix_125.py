from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='14bd9a6c-0859-5560-b258-cd2aa204563e',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name',
    display_name='Steelix',
    searchable_by=['Steelix', 'Stage 1', 'Steelix'],
    subtypes=['Stage 1'],
    collector_number=125,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=180,
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
            title='Hammer In',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
        Attack(
            title='Iron Tackle',
            game_text='This Pokémon does 50 damage to itself.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
