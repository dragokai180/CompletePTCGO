from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='51308c9e-0c3d-533c-90c4-b4f35087a972',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lucarioex.Name',
    display_name='Lucario ex',
    searchable_by=['Lucario ex', 'Stage 1', 'ex', 'Lucarioex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=17,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    family_id=448,
    abilities=[
        Attack(
            title='Low Sweep',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title='Aura Sphere',
            game_text="This attack also does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
