from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='850a29d2-78be-5d4f-9111-1ea3b613b9dd',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name',
    display_name='Shieldon',
    searchable_by=['Shieldon', 'Stage 1', 'Shieldon'],
    subtypes=['Stage 1'],
    collector_number=84,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name',
    family_id=410,
    abilities=[
        Attack(
            title='Take Down',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Confront',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
