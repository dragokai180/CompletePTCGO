from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5eb7e7a5-3353-5bc2-8042-f5b40c24168f',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Belliboltex.Name',
    display_name='Bellibolt ex',
    searchable_by=['Bellibolt ex', 'Stage 1', 'ex', 'Belliboltex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=79,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    family_id=938,
    abilities=[
        Attack(
            title='Jumping Press',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Paralyzing Ball',
            game_text="You may discard 2 Lightning Energy from this Pokémon to make your opponent's Active Pokémon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
