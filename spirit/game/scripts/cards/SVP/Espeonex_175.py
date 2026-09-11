from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="1c445a6c-a9ab-5a5a-b69e-79373f2d4e7d",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeonex.Name",
    display_name="Espeon ex",
    searchable_by=["Espeon ex", "Stage 1", "ex", "Tera", "Espeonex"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=175,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Psych Out",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title="Amazez",
            game_text="Devolve each of your opponent's evolved Pokémon by shuffling the highest Stage Evolution card on it into your opponent's deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
