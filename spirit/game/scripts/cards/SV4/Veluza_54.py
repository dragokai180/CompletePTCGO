from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='84d9ad10-1bbf-56c9-b7bc-28231a65f7ae',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name',
    display_name='Veluza',
    searchable_by=['Veluza', 'Basic', 'Veluza'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=976,
    abilities=[
        Ability(
            title='Fillet Memento',
            game_text="If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, move up to 2 Water Energy cards from this Pokémon to 1 of your Benched Pokémon.",
            passive=standard_passive("If this Pokémon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pokémon, move up to 2 Water Energy cards from this Pokémon to 1 of your Benched Pokémon."),
        ),
        Attack(
            title='Hydro Pump',
            game_text='This attack does 20 more damage for each Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
