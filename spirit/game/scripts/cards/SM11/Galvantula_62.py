from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='feb0651d-3b31-501e-ac1d-165a0739d174',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name',
    display_name='Galvantula',
    searchable_by=['Galvantula', 'Stage 1', 'Galvantula'],
    subtypes=['Stage 1'],
    collector_number=62,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name',
    family_id=595,
    abilities=[
        Attack(
            title='Live Wire',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. Also apply Weakness and Resistance for Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
