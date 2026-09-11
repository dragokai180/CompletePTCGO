from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7611cbed-f87c-5eb4-aef0-387aca6979bb',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name',
    display_name='Absol',
    searchable_by=['Absol', 'Basic', 'Absol'],
    subtypes=['Basic'],
    collector_number=88,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=359,
    abilities=[
        Ability(
            title='Dark Ambition',
            game_text="If your opponent's Active Pokémon is a Basic Pokémon, its Retreat Cost is Colorless more.",
            passive=standard_passive("If your opponent's Active Pokémon is a Basic Pokémon, its Retreat Cost is Colorless more."),
        ),
        Attack(
            title='Shadow Seeker',
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
