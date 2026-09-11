from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a9852cbf-2e01-58f0-85a7-60d7e07b3703',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name',
    display_name='Bewear',
    searchable_by=['Bewear', 'Stage 1', 'Bewear'],
    subtypes=['Stage 1'],
    collector_number=112,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    family_id=759,
    abilities=[
        Attack(
            title='Bear Hug',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Superpower',
            game_text='You may do 40 more damage. If you do, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
