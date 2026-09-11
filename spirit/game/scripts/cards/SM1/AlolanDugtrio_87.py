from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='981f6ddf-f836-5d41-87d6-ae8b6c3f6ec7',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name',
    display_name='Alolan Dugtrio',
    searchable_by=['Alolan Dugtrio', 'Stage 1', 'AlolanDugtrio'],
    subtypes=['Stage 1'],
    collector_number=87,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name',
    family_id=50,
    abilities=[
        Ability(
            title='Tangling Hair',
            game_text="Your opponent's Active Pokémon's Retreat Cost is Colorless more.",
            passive=standard_passive("Your opponent's Active Pokémon's Retreat Cost is Colorless more."),
        ),
        Attack(
            title='Dig Under',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
