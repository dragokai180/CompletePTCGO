from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7f3122db-a4e9-53f7-ab39-514b1189245d',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellibolt.Name',
    display_name='Bellibolt',
    searchable_by=['Bellibolt', 'Stage 1', 'Bellibolt'],
    subtypes=['Stage 1'],
    collector_number=77,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    family_id=938,
    abilities=[
        Attack(
            title='Electrobullet',
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
