from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5eecf87e-d3e1-5c81-acb2-cb26b76b81bb',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaDeoxysLEGEND.Name',
    display_name='Rayquaza & Deoxys LEGEND',
    searchable_by=['Rayquaza & Deoxys LEGEND', 'LEGEND', 'RayquazaDeoxysLEGEND'],
    subtypes=['LEGEND'],
    collector_number=89,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=140,
    elements=[PokemonTypes.COLORLESS, PokemonTypes.PSYCHIC],
    stage=PokemonStage.LEGEND,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    weakness_amount=2,
    family_id=384,
    abilities=[
        Ability(
            title='Space Virus',
            game_text="If your opponent's Pokémon is Knocked Out by damage from an attack of Rayquaza & Deoxys LEGEND, take 1 more Prize card.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("If your opponent's Pokémon is Knocked Out by damage from an attack of Rayquaza & Deoxys LEGEND, take 1 more Prize card."),
        ),
        Attack(
            title='Ozone Buster',
            game_text='Discard all Fire Energy attached to Rayquaza & Deoxys LEGEND.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
