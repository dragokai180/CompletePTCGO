from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6010092c-1fe1-5e43-b884-f4c73a507b93',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name',
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", 'Basic', 'Farfetchd'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=83,
    abilities=[
        Attack(
            title='Leek Slap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
