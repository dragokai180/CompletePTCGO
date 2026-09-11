from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1105f2ee-f27b-5bb1-8de2-5d266fcfb7bc',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name',
    display_name='Alolan Dugtrio',
    searchable_by=['Alolan Dugtrio', 'Stage 1', 'AlolanDugtrio'],
    subtypes=['Stage 1'],
    collector_number=122,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name',
    family_id=50,
    abilities=[
        Ability(
            title='Hair Wall',
            game_text="Your Metal Pokémon take 10 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            passive=standard_passive("Your Metal Pokémon take 10 less damage from your opponent's attacks (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
