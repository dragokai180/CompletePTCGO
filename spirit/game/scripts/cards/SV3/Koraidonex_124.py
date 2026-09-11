from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='78dd6eb0-d910-507d-9a53-1b33ed747a85',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name',
    display_name='Koraidon ex',
    searchable_by=['Koraidon ex', 'Basic', 'ex', 'Koraidonex'],
    subtypes=['Basic', 'ex'],
    collector_number=124,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=1007,
    abilities=[
        Attack(
            title='Splitting Beam',
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Gaia Press',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=standard_attack,
        ),
    ],
)
