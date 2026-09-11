from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='66c85d89-e1de-565a-a265-5b61e255fc94',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    display_name='Tadbulb',
    searchable_by=['Tadbulb', 'Basic', 'Tadbulb'],
    subtypes=['Basic'],
    collector_number=76,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=938,
    abilities=[
        Attack(
            title='Shake and Discharge',
            game_text="This attack also does 10 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
