from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1544cfbe-9e9a-5550-b623-b3e124c8f025',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Altaria.Name',
    display_name='Altaria',
    searchable_by=['Altaria', 'Stage 1', 'Altaria'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name',
    family_id=333,
    abilities=[
        Ability(
            title='Fight Song',
            game_text="Your Dragon Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("Your Dragon Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Pierce',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
