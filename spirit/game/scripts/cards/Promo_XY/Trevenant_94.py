from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='baf35887-60cc-54de-a627-a4518ab295a1',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name',
    display_name='Trevenant',
    searchable_by=['Trevenant', 'Stage 1', 'Trevenant'],
    subtypes=['Stage 1'],
    collector_number=94,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name',
    family_id=709,
    abilities=[
        Ability(
            title='Nervous Seed',
            game_text="As long as this Pokémon is your Active Pokémon, the attacks of your opponent's Basic Pokémon cost Colorless more.",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, the attacks of your opponent's Basic Pokémon cost Colorless more."),
        ),
        Attack(
            title='Energy Press',
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
