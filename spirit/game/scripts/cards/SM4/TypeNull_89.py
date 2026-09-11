from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bf599da2-4ca8-5ccc-8232-698bba431d64',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name',
    display_name='Type: Null',
    searchable_by=['Type: Null', 'Basic', 'TypeNull'],
    subtypes=['Basic'],
    collector_number=89,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=772,
    abilities=[
        Attack(
            title='Armor Press',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Claw',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
