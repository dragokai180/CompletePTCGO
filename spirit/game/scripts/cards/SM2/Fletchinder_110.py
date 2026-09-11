from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fb8f4afb-e62b-57a7-bfa2-b3fddc6b44a7',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    display_name='Fletchinder',
    searchable_by=['Fletchinder', 'Stage 1', 'Fletchinder'],
    subtypes=['Stage 1'],
    collector_number=110,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Razor Wind',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
