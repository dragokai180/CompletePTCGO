from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f1e80742-a731-5936-a737-6506cf0addbc',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name',
    display_name='Pawmot',
    searchable_by=['Pawmot', 'Stage 2', 'Pawmot'],
    subtypes=['Stage 2'],
    collector_number=76,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name',
    family_id=921,
    abilities=[
        Attack(
            title='Mach Bolt',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
        Attack(
            title='Electric Fist',
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
