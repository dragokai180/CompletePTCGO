from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9131ba4e-e429-5e81-9fce-cf2cb11c4f12',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name',
    display_name='Flaaffy',
    searchable_by=['Flaaffy', 'Stage 1', 'Flaaffy'],
    subtypes=['Stage 1'],
    collector_number=77,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name',
    family_id=179,
    abilities=[
        Attack(
            title='Signal Beam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
