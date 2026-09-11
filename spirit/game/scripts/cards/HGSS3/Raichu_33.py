from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e4eabc44-e0ee-5cbf-ba2a-9aa52d46cbd0',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name',
    display_name='Raichu',
    searchable_by=['Raichu', 'Stage 1', 'Raichu'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    family_id=25,
    abilities=[
        Attack(
            title='Pain-full Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Spark',
            game_text="Does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
