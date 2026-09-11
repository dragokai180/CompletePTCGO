from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bbffa148-dfa9-566b-828f-fd95785645b1',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name',
    display_name='Alolan Dugtrio',
    searchable_by=['Alolan Dugtrio', 'Stage 1', 'AlolanDugtrio'],
    subtypes=['Stage 1'],
    collector_number=123,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
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
        Attack(
            title='Digging Dash',
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
