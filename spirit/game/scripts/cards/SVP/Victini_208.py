from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="79097f0a-11ec-5e20-ba54-d779822322ff",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=208,
    set_code="SVP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    abilities=[
        Attack(
            title="V-Force",
            game_text="If you have 4 or fewer Benched Pokémon, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
