from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e1fd6c4e-565b-5b05-9a8a-a40652e3c637',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name',
    display_name='Zygarde',
    searchable_by=['Zygarde', 'Basic', 'Zygarde'],
    subtypes=['Basic'],
    collector_number=124,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=718,
    abilities=[
        Ability(
            title='Cellular Companions',
            game_text="As long as this Pokémon is on your Bench, your Zygarde's and Zygarde-GX's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is on your Bench, your Zygarde's and Zygarde-GX's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Boost Fang',
            game_text='Attach a Fighting Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
