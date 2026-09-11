from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6eb6ea32-5340-53d6-b32a-53a8ce66fd29',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diancie.Name',
    display_name='Diancie ◇',
    searchable_by=['Diancie ◇', 'Basic', 'Prism Star', 'Diancie'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=74,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=719,
    abilities=[
        Ability(
            title="Princess's Cheers",
            game_text="As long as this Pokémon is on your Bench, your Fighting Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is on your Bench, your Fighting Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Diamond Rain',
            game_text='Heal 30 damage from each of your Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
