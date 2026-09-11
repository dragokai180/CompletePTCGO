from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="046f68f6-0f78-5904-baf4-1b19d4a45829",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPersianex.Name",
    display_name="Team Rocket's Persian ex",
    searchable_by=["Team Rocket's Persian ex", "Stage 1", "ex", "TeamRocketsPersianex"],
    subtypes=["Stage 1", "ex"],
    collector_number=218,
    set_code="SVP",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMeowth.Name",
    abilities=[
        Attack(
            title="Haughty Order",
            game_text="Reveal the top 10 cards of your opponent's deck. You may choose an attack from a Pokémon you find there and use it as this attack. Shuffle the revealed cards into your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title="Cruel Slash",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
